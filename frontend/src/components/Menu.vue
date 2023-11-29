<script setup lang="ts">
import { ref, onMounted, readonly } from 'vue'

const menuItems = ref([
  { name: 'Arabidopsis thaliana' },
  { name: 'Abscisic acid' },
  { name: 'Auxin' },
  { name: 'Brassinosteroid' },
  { name: 'Cytokinin' },
  { name: 'Ethylene' },
  { name: 'Gibberellin' },
  { name: 'Jasmonic acid' },
  { name: 'Salicylic acid' },
  { name: 'Strigolactone' },
  { name: 'Oryza sativa' },
  { name: 'Glycine max' },
  { name: 'Zea mays' }
])

const tableHeaders = ref([
  { text: 'Rank', value: 'rank' },
  { text: 'Pocket ID', value: 'pocketId' },
  { text: 'Binding affinity (kcal/mol)', value: 'bindingAffinity' },
  { text: 'Uniprot ID', value: 'uniprotId' },
  { text: 'Description', value: 'description' },
  { text: 'PDB ID', value: 'pdbId' }
])

const itemsPerPage = ref(10)
const totalItems = ref(0)
const serverItems =ref([])
interface LoadItemsParams {
  page: number;
  itemsPerPage: number;
}

const resultHeaders = readonly(ref([
  { title: 'Uniprot_id', value: 'uniprot_id', align: 'start'},
  { title: 'Protein names', value: 'protein_names', align: 'start' },
  { title: 'Gene names', value: 'gene_names', align: 'start' },
  { title: 'Organism', value: 'organism', align: 'start' },
  { title: 'PDB ID', value: 'pdb', align: 'start' },
  { title: 'Pocket ID', value: 'pocket_id', align: 'start' },
  { title: 'Binding affinity', value: 'binding_affinity', align: 'start' }
]))

</script>

<template>
  <v-app>
    <v-navigation-drawer app>
      <v-list accordion dense>
        <v-list-group v-for="item in menuItems" :key="item.name" no-action>
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </template>
          <!-- Sub-items here if needed -->
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-icon icon="@/assets/PokeVA.svg" alt="Logo" />
      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Search"
        prepend-inner-icon="mdi-magnify"
      ></v-text-field>
    </v-app-bar>
    <v-main>
      <v-data-table-server
        :items-per-page="itemsPerPage"
        :headers="resultHeaders"
        :items-length="totalItems"
        :items="serverItems"
        loading=true
        @update:options="loadItems"
      ></v-data-table-server>
    </v-main>
  </v-app>
</template>
