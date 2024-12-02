<template>  
    <v-form v-model="valid">  
      <v-container>  
        <v-row>  
          <v-col cols="12" md="6">  
            <v-text-field  
              v-model="username"  
              :rules="usernameRules"  
              label="Username"  
              required  
            ></v-text-field>  
          </v-col>  
  
          <v-col cols="12" md="6">  
            <v-text-field  
              v-model="password"  
              :rules="passwordRules"  
              label="Password"  
              type="password"  
              required  
            ></v-text-field>  
          </v-col>  
        </v-row>  
  
        <v-row>  
          <v-col cols="12">  
            <v-btn @click="login" :disabled="!valid" color="primary">Login</v-btn>  
          </v-col>  
        </v-row>  
      </v-container>  
    </v-form>  
  </template>  
  
  <script>  
  import axios from 'axios';  
  
  export default {  
    data: () => ({  
      valid: false,  
      username: '',  
      password: '',  
      usernameRules: [  
        value => {  
          if (value) return true  
          return 'Username is required.'  
        },  
        value => {  
          if (value.length >= 3) return true  
          return 'Username must be at least 3 characters long.'  
        }  
      ],  
      passwordRules: [  
        value => {  
          if (value) return true  
          return 'Password is required.'  
        }  
      ]  
    }),  
  
    methods: {  
      async login() {  
        if (this.valid) {  
          try {  
            const response = await axios.post('http://127.0.0.1:8000/userProfile/login/', {  
              username: this.username,  
              password: this.password  
            });  
  
            console.log('Login successful:', response.data); 
 
 
          } catch (error) {  
            console.error('Login failed:', error.response?.data || error.message);  
            alert('Login failed: ' + (error.response?.data?.error || 'An error occurred. Please try again.'));  
          }  
        }  
      }  
    }  
  }  
  </script>  
  
