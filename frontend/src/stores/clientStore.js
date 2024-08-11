// stores/clientStore.js

import {defineStore} from 'pinia'

export const clientStore = defineStore('clientStore', {
  state: () => ({
    isSidebarOpen: true,
  }),
  actions: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
  },
  persist: true,
})
