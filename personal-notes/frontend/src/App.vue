<template>
  <v-app>
    <v-layout>
      <Navbar />
      <VerticalNavbar />
      <v-main>
        <ViewNotes />
      </v-main>
    </v-layout>
    


    
  </v-app>
</template>

<script setup>
  import Navbar from './components/Navbar.vue';
  import VerticalNavbar from './components/VerticalNavbar.vue';
  import ViewNotes from './components/ViewNotes.vue';
  import StartingPage from './pages/StartingPage.vue';
</script>

