<template>  
    <v-dialog v-model="dialogVisible" max-width="600">  
        <template v-slot:activator="{ props: activatorProps }">  
            <v-btn  
                v-bind="activatorProps"  
                color="surface-variant"  
                text="Add Note"  
                variant="outlined"  
                prepend-icon="mdi-plus"  
            ></v-btn>  
        </template>  

        <v-card title="Create a new note">  
            <v-form @submit.prevent="handleSubmit">  
                <v-text-field  
                    v-model="title"  
                    :rules="rules"  
                    hide-details="auto"  
                    label="Title"  
                ></v-text-field>  
                <v-textarea  
                    clearable  
                    v-model="content"  
                    label="Write your note here"  
                    :rules="rules"  
                ></v-textarea>  
                <v-spacer></v-spacer>  

                <v-card-actions class="d-flex justify-space-between align-center ma-2">  
                    <v-btn text="Add" type="submit"></v-btn>  
                    <v-btn text="Cancel" @click="closeDialog"></v-btn>  
                </v-card-actions>  
            </v-form>  
        </v-card>  
    </v-dialog>  
</template>  

<script setup>  
import { ref, defineEmits } from 'vue';  
import { useDate } from 'vuetify';  

const date = useDate();  
const dialogVisible = ref(false); // State to control dialog visibility  
const title = ref('');  
const content = ref('');  
const newNote = ref({});  
const emit = defineEmits(['addNote']);  

const rules = [  
    value => !!value || 'Required.',  
    value => (value && value.length >= 3) || 'Min 3 characters',  
];  

const handleSubmit = () => {  
    newNote.value = {  
        title: title.value,  
        content: content.value,  
        date: date.format('YYYY-MM-DD', 'fullDate'),  
    };  
    emit('addNote', newNote.value);  
    closeDialog(); // Close dialog after submission  
};  

const closeDialog = () => {  
    dialogVisible.value = false; // Close the dialog  
};  

// Optionally, you could create a function to open the dialog when needed  
const openDialog = () => {  
    dialogVisible.value = true; // Open the dialog  
};  
</script>  

<style scoped>  
/* Add any specific styles you want here */  
</style>