<template>  
  <v-dialog max-width="600">  
    <template v-slot:activator="{ props: activatorProps }">  
      <v-card   
        v-if="note"   
        class="w-100"  
        v-bind="activatorProps">  
        <div class="d-flex justify-space-between align-center">  
          <v-card-title>{{ note.title }}</v-card-title>  
          <v-card-subtitle>{{ note.date }}</v-card-subtitle>  
        </div>  
        <v-card-text>{{ note.content }}</v-card-text>  
      </v-card>  
    </template>  

    <template v-slot:default="{ isActive }">  
      <v-card>  
        <v-card-title>{{ note.title }}</v-card-title>  
        
        <v-card-text v-if="!shouldEdit">  
          {{ note.content }}  
        </v-card-text>  
        
        <v-textarea   
          v-if="shouldEdit"  
          v-model="note.content"   
          clearable   
          label="Edit Note"  
          :rules="rules"
        ></v-textarea>  

        <v-card-actions>  
          <v-spacer></v-spacer>  
          <v-btn  
            text="edit"  
            v-if="!shouldEdit"  
            @click="shouldEdit = true"  
          ></v-btn>  
          <v-btn  
            text="save"  
            v-if="shouldEdit"  
            @click="saveNote"  
          ></v-btn>  
          <v-btn  
            text="delete"  
            @click="deleteNote"  
          ></v-btn>  
        </v-card-actions>  
      </v-card>  
    </template>  
  </v-dialog>  
</template>  

<script setup>  
import { ref,defineEmits } from 'vue';  


const rules=[
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ]
const props = defineProps(['note']);  
const emit = defineEmits(['deleteNote']);
const shouldEdit = ref(false);  
 
onMounted(() => {
  axios.get(`http://127.0.0.1:8000/api/notes/`)
        .then(response => {
         console.log(response.data);
})
})
const saveNote = () => {  
  shouldEdit.value = false;  
};  


const deleteNote = () => {  
  emit('deleteNote', props.note);
  isActive.value = false; 
};  
</script>