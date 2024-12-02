<template>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="username"
              :rules="nameRules"
              label="User name"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              label="Password"
              required
            ></v-text-field>
          </v-col>
  
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="confirmPassword"
              :rules="passwordRules"
              label="Confirm Password"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>  
          <v-col cols="12">  
            <v-btn @click="register" :disabled="!valid" color="primary">Register</v-btn>  
          </v-col>  
        </v-row>
      </v-container>
    </v-form>
  </template>
  <script>
  export default {
    data: () => ({
      valid: false,
      username: '',
      
      nameRules: [
        value => {
          if (value) return true

          return 'User name is required.'
        },
        value => {
          if (value?.length >= 3) return true

          return 'Name must be more than characters.'
        },
      ],
      email: '',
      emailRules: [
        value => {
          if (value) return true

          return 'E-mail is required.'
        },
        value => {
          if (/.+@.+\..+/.test(value)) return true

          return 'E-mail must be valid.'
        },
      ],
      password: '',
      confirmPassword: '',
      passwordRules: [
        value => {
          if (value) return true

          return 'Password is required.'
        },
        value => {
          if (this.confirmPassword && value !== this.confirmPassword) {
            return 'Passwords do not match'
          }

          return true
        },
      ],
    }),
    methods: {
      async register() {  
        if (this.valid) {  
          try {  
            const response = await axios.post('/userProfile/register/', {  
              username: this.username,  
              email: this.email,  
              password: this.password  
            });  
            console.log('Registration successful:', response.data);  
            
          } catch (error) {  
            console.error('Registration failed:', error.response?.data || error.message);  
            alert('Registration failed: ' + (error.response?.data?.error || 'An error occurred. Please try again.'));  
          }  
        }  
      },
    },
  }
</script>
