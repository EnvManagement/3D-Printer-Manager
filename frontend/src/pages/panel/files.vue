<template>
  <v-container fluid>
    <!-- Header -->
    <v-row>
      <v-col cols="12">
        <v-toolbar dense flat>
          <v-toolbar-title>Your Files</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search for a file"
            single-line
            hide-details
          ></v-text-field>
          <v-btn icon @click="toggleFilter">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
          <v-menu v-model="filterVisible" offset-y>
            <v-card>
              <v-card-title>Filter files</v-card-title>
              <v-card-text>
                <v-combobox
                  v-model="selectedPrinters"
                  :items="printers"
                  label="Select printers"
                  multiple
                ></v-combobox>
                <v-checkbox v-model="filterGCODE" label="GCODE"></v-checkbox>
                <v-checkbox v-model="filterSTL" label="STL"></v-checkbox>
                <v-checkbox v-model="filter3MF" label="3MF"></v-checkbox>
                <v-checkbox v-model="filterOBJ" label="OBJ"></v-checkbox>
                <v-select
                  v-model="selectedMaterial"
                  :items="materials"
                  label="Material"
                ></v-select>
                <v-select
                  v-model="selectedSlicer"
                  :items="slicers"
                  label="Slicer"
                ></v-select>
              </v-card-text>
            </v-card>
          </v-menu>
          <v-btn icon @click="uploadFile">
            <v-icon>mdi-upload</v-icon>
          </v-btn>
          <v-btn icon @click="createFolder">
            <v-icon>mdi-folder-plus</v-icon>
          </v-btn>
          <v-btn icon @click="toggleView">
            <v-icon>{{ gridView ? 'mdi-view-list' : 'mdi-view-grid' }}</v-icon>
          </v-btn>
        </v-toolbar>
      </v-col>
    </v-row>

    <!-- Main Content -->
    <v-row>
      <v-col cols="8">
        <v-row>
          <v-col
            v-for="file in files"
            :key="file.name"
            cols="12"
            md="6"
            lg="4"
            @click="selectFile(file)"
            @contextmenu.prevent="openContextMenu($event, file)"
          >
            <v-card outlined :class="{ 'v-card--hover': gridView }">
              <v-img :src="file.preview" :alt="file.name" height="150px"></v-img>
              <v-card-title>{{ file.name }}</v-card-title>
              <v-card-subtitle>{{ file.size }}</v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-col>

      <!-- File Preview -->
      <v-col cols="4" v-if="selectedFile">
        <v-card>
          <v-card-title>
            {{ selectedFile.name }}
            <v-spacer></v-spacer>
            <v-btn icon @click="selectedFile = null">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-subtitle>{{ selectedFile.size }}</v-card-subtitle>
          <v-img :src="selectedFile.preview" alt="Preview" height="200px"></v-img>
          <v-list>
            <v-list-item>
              <v-list-item-content>Times printed: {{ selectedFile.timesPrinted }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>Size: {{ selectedFile.dimensions }}</v-list-item-content>
            </v-list-item>
          </v-list>
          <v-btn @click="addToPrintQueue">Add to print queue</v-btn>
        </v-card>
      </v-col>
    </v-row>

    <!-- Context Menu -->
    <v-menu
      v-model="contextMenuVisible"
      :position-x="contextMenu.x"
      :position-y="contextMenu.y"
      absolute
    >
      <v-list>
        <v-list-item @click="deleteFile(selectedFile)">Delete</v-list-item>
        <v-list-item @click="downloadFile(selectedFile)">Download</v-list-item>
        <v-list-item @click="renameFile(selectedFile)">Rename</v-list-item>
        <v-list-item @click="moveFile(selectedFile)">Move</v-list-item>
        <v-list-item @click="addToPrintQueue">Add to print queue</v-list-item>
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
      filterVisible: false,
      selectedPrinters: [],
      filterGCODE: false,
      filterSTL: false,
      filter3MF: false,
      filterOBJ: false,
      selectedMaterial: null,
      selectedSlicer: null,
      printers: ['Printer 1', 'Printer 2'],
      materials: ['PLA', 'ABS', 'PETG'],
      slicers: ['Slicer 1', 'Slicer 2'],
      files: [
        {
          name: 'hairpin.stl',
          size: '15 MB',
          preview: 'path-to-preview-image',
          timesPrinted: 0,
          dimensions: '83 x 127 x 65 mm',
        },
      ],
      selectedFile: null,
      contextMenuVisible: false,
      contextMenu: {x: 0, y: 0},
    };
  },
  methods: {
    toggleFilter() {
      this.filterVisible = !this.filterVisible;
    },
    uploadFile() {
      // Logic to upload file
    },
    createFolder() {
      // Logic to create a new folder
    },
    toggleView() {
      this.gridView = !this.gridView;
    },
    selectFile(file) {
      this.selectedFile = file;
    },
    openContextMenu(event, file) {
      this.contextMenuVisible = true;
      this.contextMenu = {x: event.clientX, y: event.clientY};
      this.selectedFile = file;
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
    addToPrintQueue() {
      // Logic to add the file to the print queue
    },
  },
};
</script>

<style scoped>
.v-card--hover {
  transition: 0.3s ease-in-out;
  cursor: pointer;
}

.v-card--hover:hover {
  transform: scale(1.05);
}
</style>
