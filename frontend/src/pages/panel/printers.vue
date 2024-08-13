<template>
  <v-container fluid>
    <!-- Top Section with Printer Name and Buttons -->
    <v-row>
      <v-col cols="12">
        <v-card flat>
          <v-card-title class="d-flex justify-content-between align-items-center">
            <span class="text-center" style="font-size: 2rem;">Ultimaker 2 Go</span>
            <div>
              <v-btn icon="mdi-cog"/>
              <v-btn icon="mdi-refresh"/>
            </div>
          </v-card-title>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <!-- Printer Details Section -->
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>
            <v-icon color="red" class="mr-2">mdi-alert-circle</v-icon>
            Not connected
          </v-card-title>
          <v-card-text class="text-center">
            <v-img
              src="https://cdn.simplyprint.io/i/printer_types/ultimaker/2_go/product_photo_md.png?cacheid=60180ee5c2a98"
              aspect-ratio="1"/>
          </v-card-text>
          <v-card-text>
            <v-btn color="primary" @click="dialog = true">Open Edit Material</v-btn>

            <!-- Dialog -->
            <v-dialog v-model="dialog" max-width="600" inverted>
              <v-card class="pa-4">
                <v-card-title>
                  <v-btn @click="back" icon="mdi-arrow-left" class="mr-1"/>
                  Edit material
                </v-card-title>

                <v-card-text>

                  <v-form>
                    <h6 class="text-center mb-0 font-weight-bold" style="font-size: 18px;">Assign specific spool</h6>
                    <v-btn-toggle>
                      <v-btn outlined color="primary" icon="mdi-package-variant-closed">
                        <v-icon>mdi-package-variant-closed</v-icon>
                        Pick new spool
                      </v-btn>
                      <v-btn color="primary" outlined v-if="spoolOptions.length">
                        <v-icon>mdi-chevron-down</v-icon>
                      </v-btn>
                    </v-btn-toggle>
                    <!-- Material Type -->
                    <v-select :items="materialTypes" label="Material type" v-model="selectedMaterial" outlined/>

                    <!-- Color Selection -->
                    <v-color-picker v-model="selectedColor" mode="hexa"/>

                    <!-- Save Button -->
                    <v-btn block outlined color="primary" class="mt-2" :disabled="!canSave">Save material data</v-btn>
                  </v-form>
                </v-card-text>
              </v-card>
            </v-dialog>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Control and Temperature Section -->
      <v-col cols="12" md="4">

        <!-- Control Section -->
        <v-card>
          <v-card-title>Control</v-card-title>
          <v-spacer/>
          <v-card-text>

            <v-row justify="center">
              <v-col>
                <v-btn block color="primary" class="mb-1" icon="mdi-arrow-up"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-home"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-arrow-down"/>
              </v-col>

              <v-col>
                <v-btn block color="primary" class="mt-13" icon="mdi-arrow-left"/>
              </v-col>

              <v-col>
                <v-btn block color="primary" class="mb-1" icon="mdi-arrow-up"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-home"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-arrow-down"/>
              </v-col>

              <v-col>
                <v-btn block color="primary" class="mt-13" icon="mdi-arrow-right"/>
              </v-col>

              <v-col>
                <v-btn block color="primary" class="mb-1" icon="mdi-plus"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-alpha-e"/>
                <v-btn block color="primary" class="mb-1" icon="mdi-minus"/>
              </v-col>
            </v-row>

            <v-row class="mt-10">
              <v-col>
                <v-text-field label="Change print speed" suffix="%" type="number"></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-text-field label="Control flow rate" suffix="%" type="number"></v-text-field>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>

        <!-- Temperature Section -->
        <v-card class="mt-4">
          <v-card-title>Temperatures</v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="2">
                <v-text-field suffix="°" type="number" v-model="printer.nozzleTemperature" readonly/>
              </v-col>
              <v-col>
                <v-text-field label="Nozzle" suffix="°" type="number"/>
              </v-col>
            </v-row>
            <v-btn block color="primary">Set Temperatures</v-btn>
            <v-row class="mt-3">
              <v-col>
                <v-btn block color="primary">Preheat</v-btn>
              </v-col>
              <v-col>
                <v-btn block color="primary">Cooldown</v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Webcam Section -->
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>Webcam</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      printer: {
        nozzleTemperature: 50,
      },
      sliderValue: 10,
      selectedFilament: '',
      selectedColor: '#000000', // Default color selection
      materialTypes: ['PLA', 'ABS', 'ASA', 'PETG', 'TPU/TPE', 'Nylon', 'Polycarbonate', 'HIPS', 'PVA', 'PMMA'],
      selectedMaterial: null,
      spoolOptions: ['Create new spool'], // Example dropdown options
      canSave: false, // Logic for enabling/disabling the save button
    };
  },
  methods: {
    back() {
      // Handle back button action
    },
    showInfo() {
      // Handle info button action
    },
  },
};
</script>

<style scoped>

.v-btn {
  border-radius: 4px
}

</style>
