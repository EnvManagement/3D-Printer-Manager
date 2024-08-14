<template>
    <v-container class="fill-height d-flex justify-center align-center">
      <v-card class="text-center" style="border-radius: 25px; padding: 5rem;">
        <v-card-title>
          <v-icon size="10rem" color="grey" icon="mdi-alert-octagon-outline"/>
        </v-card-title>
        <v-card-subtitle class="text-h2">
          404
        </v-card-subtitle>
        <v-card-text>
          <p class="text-h6 mb-4">Oops! The page you're looking for doesn't exist.</p>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn @click="$router.back" color="grey" text="Go Back" prepend-icon="mdi-arrow-left"
                 style="border-radius: 10px; font-size: 1.25rem;"/>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <!-- This is here so that $router is recognized -->
  <script>
  </script>
  