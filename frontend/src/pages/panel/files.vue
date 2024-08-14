<template>
  <v-container fluid>
    <!-- Header -->
    <v-row>
      <v-col cols="12">
        <v-card flat>
          <v-card-title class="d-flex justify-content-between align-items-center">
            <span style="font-size: 2rem">Your Files</span>
            <v-spacer/>
            <div>
              <v-btn icon="mdi-upload"/>
              <v-btn icon="mdi-folder-plus"/>
              <v-btn :icon="gridView ? 'mdi-view-list' : 'mdi-view-grid'" @click="gridView = !gridView"/>
            </div>
          </v-card-title>
          <v-text-field v-model="search" label="Search for a file" prepend-inner-icon="mdi-magnify"
                        style="margin: 0 1rem">
            <template v-slot:append-inner>
              <v-btn icon="mdi-filter" @click="filter.visible = !filter.visible"/>
            </template>
          </v-text-field>

          <!-- Filter Section -->
          <v-expand-transition>
            <v-card v-if="filter.visible" flat class="pa-3">
              <v-row>
                <v-col cols="8">
                  <v-select v-model="filter.printers" :items="printers" label="Select printers" multiple chips/>
                </v-col>
                <v-col cols="1">
                  <v-checkbox v-model="filter.GCODE" label="GCODE"/>
                </v-col>
                <v-col cols="1">
                  <v-checkbox v-model="filter.STL" label="STL"/>
                </v-col>
                <v-col cols="1">
                  <v-checkbox v-model="filter['3MF']" label="3MF"/>
                </v-col>
                <v-col cols="1">
                  <v-checkbox v-model="filter.OBJ" label="OBJ"/>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="8">
                  <v-select v-model="filter.materials" :items="materials" label="Material" multiple chips/>
                </v-col>
                <v-col cols="2">
                  <v-checkbox v-model="filter.searchInCurrentFolder" label="Only search in current folder"/>
                </v-col>
              </v-row>
            </v-card>
          </v-expand-transition>

        </v-card>
      </v-col>
    </v-row>

    <!-- Main Content -->
    <v-row>
      <v-col :cols="12">
        <!-- Grid View -->
        <v-row v-if="gridView">
          <v-col v-for="(file, index) in files" :key="index" cols="12" lg="4">
            <v-card class="v-card--hover" style="display: flex; height: 100px;"
                    @contextmenu.prevent="openContextMenu($event, file)">
              <div style="display: flex; align-items: center;">
                <v-img :src="file.preview" :alt="file.name" width="5rem"/>
                <div>
                  <v-card-title style="font-size: 14px;">{{ file.name }}</v-card-title>
                  <v-card-subtitle style="font-size: 12px;">{{ file.size }}</v-card-subtitle>
                </div>
              </div>
            </v-card>
          </v-col>
        </v-row>

        <!-- List View -->
        <v-row v-else>
          <v-col cols="12">
            <v-data-table
              :headers="[{ title: 'Name', key: 'name'},{ title: 'Date', key: 'date' },{ title: 'Size', key: 'size' },]"
              :items="files"
              item-class="d-flex align-center"
              :item-clickable="true"
              @contextmenu.prevent="openContextMenu($event, item)"
            />
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Context Menu -->
    <v-menu v-model="contextMenu.visible" style="position: absolute;"
            :style="{ top: `${contextMenu.y}px`, left: `${contextMenu.x}px` }">
      <v-list>
        <v-list-subheader>{{ contextMenu.file.name }}</v-list-subheader>
        <v-divider/>
        <v-list-item @click="deleteFile(contextMenu.file)">
          <v-icon icon="mdi-delete" class="mr-2"/>
          Delete
        </v-list-item>
        <v-list-item @click="downloadFile(contextMenu.file)">
          <v-icon icon="mdi-download" class="mr-2"/>
          Download
        </v-list-item>
        <v-list-item @click="renameFile(contextMenu.file)">
          <v-icon icon="mdi-rename-box" class="mr-2"/>
          Rename
        </v-list-item>
        <v-list-item @click="moveFile(contextMenu.file)">
          <v-icon icon="mdi-folder-move" class="mr-2"/>
          Move
        </v-list-item>
        <v-list-item @click="addToQueue(contextMenu.file)">
          <v-icon icon="mdi-playlist-plus" class="mr-2"/>
          Add to print queue
        </v-list-item>
      </v-list>
    </v-menu>
  </v-container>
</template>


<script>
export default {
  data() {
    return {
      search: '',
      gridView: true,
      filter: {
        visible: false
      },
      printers: ['Printer 1', 'Printer 2'],
      materials: ['PLA', 'ABS', 'PETG'],
      files: [
        {
          name: 'hairpin.stl',
          date: '2024-08-14',
          size: '15 MB',
          preview: 'https://cdn.simplyprint.io/i/user/file/69b8bbec34a048ff9b02f396886d07bb.png?v=2',
          timesPrinted: 0,
          dimensions: '83 x 127 x 65 mm',
        },
        {
          name: 'hairpin.stl',
          date: '2024-08-14',
          size: '15 MB',
          preview: 'https://cdn.simplyprint.io/i/user/file/69b8bbec34a048ff9b02f396886d07bb.png?v=2',
          timesPrinted: 0,
          dimensions: '83 x 127 x 65 mm',
        },
        {
          name: 'hairpin.stl',
          date: '2024-08-14',
          size: '15 MB',
          preview: 'https://cdn.simplyprint.io/i/user/file/69b8bbec34a048ff9b02f396886d07bb.png?v=2',
          timesPrinted: 0,
          dimensions: '83 x 127 x 65 mm',
        },
      ],
      contextMenu: {
        visible: false,
        x: 0,
        y: 0,
        file: null,
      },
    };
  },
  methods: {
    openContextMenu(event, file) {
      this.contextMenu.visible = true;
      this.contextMenu.x = event.clientX;
      this.contextMenu.y = event.clientY;
      this.contextMenu.file = file;
    },
    deleteFile(file) {
      // Logic to delete the file
    },
    downloadFile(file) {
      // Logic to download the file
    },
    renameFile(file) {
      // Logic to rename the file
    },
    moveFile(file) {
      // Logic to move the file
    },
    addToQueue(file) {
      // Logic to add the file to the print queue
    },
    closeContextMenu() {
      this.contextMenu.visible = false;
    }
  },
  mounted() {
    window.addEventListener('click', this.closeContextMenu);
  },
  beforeDestroy() {
    window.removeEventListener('click', this.closeContextMenu);
  },
};
</script>

<style scoped>
.v-card--hover {
  transition: 0.3s ease-in-out;
}

.v-card--hover:hover {
  transform: scale(1.01);
}
</style>
