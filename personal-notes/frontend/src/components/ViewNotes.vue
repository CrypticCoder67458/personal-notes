<template>
    <v-container class="ps-16 mb-15 d-flex justify-center flex-column"
   >
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
        <AddNoteButton  @addNote="addNote" />
      </div>
    </v-container>
  </template>
  
  <script setup>
  import Note from './Note.vue';
  import AddNoteButton from './AddNoteButton.vue';
  import { ref } from 'vue';

  const notes = ref([
  ]);
  const addNote = (note) => {
    if (!note.content || !note.title) return;
    notes.value.push(note);
  }
  const deleteNote = (note) => {
    notes.value = notes.value.filter((n) => n !== note);
  }
  </script>
  