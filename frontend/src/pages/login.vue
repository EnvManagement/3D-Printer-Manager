<template>
  <v-app>
    <v-container class="d-flex align-center justify-center" style="height: 100vh;">
      <v-card class="pa-8" max-width="600">
        <v-card-title class="text-h5">3D Printer Management System</v-card-title>
        <v-card-text>
          <p>
            Welcome to the 3D Printer Management System. Here, you can create bookings, monitor
            printers, initiate print jobs, see available filaments, and request new filaments.
          </p>
        </v-card-text>
        <v-card-actions class="d-flex flex-column">
          <v-btn @click="login" color="primary" class="mb-2" block>
            Oauth Login
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    async login() {
      const path = `${this.$backend_url}login`;
      const res = await axios.get(path, {withCredentials: true});
      window.location.href = res.data['auth_url'];
    },
  },
  mounted() {
    if (this.$currentUser) {
      this.$router.push('/');
    }
  },
};
</script>
