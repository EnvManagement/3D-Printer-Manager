<template>
  <v-app>
    <v-navigation-drawer
      :rail="!clientSettings.isSidebarOpen">
      <v-list style="overflow: hidden">
        <v-list-item>
          <v-img src="@/assets/logo.svg" height="100"></v-img>
        </v-list-item>
        <v-list-item v-for="(button, index) in sidebarButtons" :key="index" link :to="button.link"
                     :style="{ marginBottom: button.gap }">
          <v-icon :icon="button.icon"/>
          <div v-show="clientSettings.isSidebarOpen" style="margin-left: 15px; display: inline;">{{ button.text }}</div>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="clientSettings.toggleSidebar"/>
      <v-app-bar-title>3D Printer Management System</v-app-bar-title>
      <v-btn @click="toggleTheme">
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>
      <v-btn>
        <v-icon>mdi-account</v-icon>
        Dominik Kovacs
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import {clientStore} from '@/stores/clientStore'
import {useTheme} from 'vuetify'

export default {
  setup() {
    const theme = useTheme()
    const clientSettings = clientStore()

    return {clientSettings, theme}
  },
  data() {
    return {
      sidebarButtons: [
        {
          icon: 'mdi-printer-3d',
          text: 'Printers',
          link: '/panel/printers',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-folder-open',
          text: 'Your Files',
          link: '/panel/files',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-queue-first-in-last-out',
          text: 'Queue',
          link: '/panel/queue',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-chart-line',
          text: 'Statistics',
          link: '/panel/statistics',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-folder-open',
          text: 'Your Files',
          link: '/panel/files',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-history',
          text: 'Print History',
          link: '/panel/jobs',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-palette-swatch',
          text: 'Filament',
          link: '/panel/filament',
          gap: '0.5rem'
        },
        {
          icon: 'mdi-hexagon-slice-2',
          text: 'Slicer',
          link: '/panel/slicer',
          gap: '0.5rem'
        },
      ],
    }
  },
  methods: {
    toggleTheme() {
      this.theme.global.name.value = this.theme.global.current.value.dark ? 'light' : 'dark'
    }
  }
}
</script>
