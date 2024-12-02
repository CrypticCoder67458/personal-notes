<template>
    <div class="d-flex flex-column justify-center align-center"> 
        <h1>Hey, you need to register/login to use this app</h1>
        <div class="d-flex justify-center align-center mt-10 ga-sm-5">
            <router-link to="/register">            
                <v-btn>register</v-btn>
            </router-link>

            <router-link to="/login">
                <v-btn>login</v-btn>
            </router-link>
        </div>
        
    </div>
</template>

<script setup>
</script>