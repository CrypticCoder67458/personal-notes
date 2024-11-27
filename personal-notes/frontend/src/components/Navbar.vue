<template>
    <v-app-bar :elevation="2" class="mb-10">
        <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

    <v-app-bar-title>Application Bar</v-app-bar-title>
    <svg-icon 
        type="mdi" 
        :path=mdiAccountCircle 
        class="mr-4" 
        size="2em"
    ></svg-icon>
    </v-app-bar>
</template>
<script setup>
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiAccountCircle } from '@mdi/js';
</script>