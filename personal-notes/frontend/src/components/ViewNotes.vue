<template>  
  <v-container class="ps-16 mb-15 d-flex justify-center flex-column">  
      <h2>View Notes:</h2>  
      <v-row class="flex-nowrap">  
          <v-col cols="12" class="flex-grow-1 flex-shrink-1">  
              <div v-for="(note, index) in notes"   
                  :key="index"   
                  class="mb-5 w-100">  
                  <Note   
                      :note="note"   
                      class="w-100"   
                      @deleteNote="deleteNote"/>  
              </div>  
          </v-col>  
      </v-row>  
      <div class="d-flex justify-end mt-4">  
          <AddNoteButton @addNote="addNote" />  
      </div>  
  </v-container>  
</template>  

<script setup>  
import Note from './Note.vue';  
import AddNoteButton from './AddNoteButton.vue';  
import { onMounted, ref } from 'vue';  
import axios from 'axios';  

const notes = ref([]);  

// Fetch notes on component mount  
onMounted(() => {  
  fetchNotes();  // Fetch notes into the local state  
});  

// Fetch notes from the server  
const fetchNotes = () => {  
  axios.get('http://127.0.0.1:8000/notes/')  
      .then(response => {  
          notes.value = response.data; // Store the response data in the notes ref  
      })  
      .catch(error => {  
          console.error("There was an error!", error);  
      });  
}  

// Handle adding a new note  
const addNote = (note) => {  
  console.log('submitted', note);  
  axios.post('http://127.0.0.1:8000/notes/', note) // Send note directly  
      .then(response => {  
          // Integrate the new note into the local state  
          notes.value.push(response.data);   
          console.log('Note added:', response.data);  
      })  
      .catch(error => {  
          console.error('Error while adding note:', error);  
      })  
}  

// Handle deleting a note  
const deleteNote = (note) => {  
  axios.delete(`http://127.0.0.1:8000/notes/${note.id}/`) // Assuming your API follows REST conventions  
      .then(() => {  
          notes.value = notes.value.filter((n) => n.id !== note.id); // Update local state after deletion  
          console.log('Note deleted:', note);  
      })  
      .catch(error => {  
          console.error('Error while deleting note:', error);  
      });  
}  
</script>  

<style scoped>  
/* Add any specific styles you want here */  
</style>
  