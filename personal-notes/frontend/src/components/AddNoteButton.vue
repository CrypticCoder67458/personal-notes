<template>
    <v-dialog max-width="600">
    <template v-slot:activator="{ props: activatorProps }">

        <v-btn
        v-bind="activatorProps"
        color="surface-variant"
        text="Add Note"
        variant="outlined" 
        prepend-icon="mdi-plus"
        ></v-btn>
    </template>

    <template v-slot:default="{ isActive }">
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
                        label="write your note here"
                        :rules="rules"
                ></v-textarea>
                <v-spacer></v-spacer>
                
                    
                <v-card-actions 
                class="d-flex justify-space-between align-center ma-2">
                    <v-btn
                    text="add"
                    type="submit"
                    @click="isActive.value = false"
                    ></v-btn>
                    <v-btn
                    text="cancel "
                    @click="isActive.value = false"
                    ></v-btn>
                </v-card-actions>   
            </v-form>

        </v-card>
    </template>
</v-dialog>
</template>


<script setup>
import { ref ,defineEmits} from 'vue'
import { useDate } from 'vuetify'

    const date = useDate()
    const rules=[
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ]
    const title = ref('');
    const content = ref('');
    const newNote = ref({});
    

    const emit = defineEmits(['addNote'])

    const handleSubmit = () => {
        newNote.value = {
            title: title.value,
            content: content.value,
            date: date.format('YYYY-MM-DD', 'fullDate'),
        }
        emit('addNote', newNote.value);
        title.value = '';
        content.value = '';
    }

</script>