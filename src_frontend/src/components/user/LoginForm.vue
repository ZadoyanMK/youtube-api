<template>
    <v-dialog
        v-model="dialog"
        content-class="form-style"
        persistent 
    >
        <v-card class="elevation-12">
              <v-toolbar color="grey lighten-2">
                <v-toolbar-title>Login form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form
                  ref="form" 
                  v-model="valid"
                  lazy-validation>

                  <v-text-field 
                  v-model="username"
                  prepend-icon="person" 
                  name="username" 
                  label="Username"
                  :rules="usernameRules"
                  type="text"/>

                  <v-text-field
                  v-model="password"
                  prepend-icon="lock" 
                  name="password" 
                  label="Password" 
                  id="password"
                  :rules="passwordRules"
                  type="password" />
                </v-form>
                <ul>
                  <li class="red--text subheading" v-for="err in errors">
                    {{err}}
                  </li>
                </ul>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn 
                  flat 
                  color="red darken-2" 
                  @click="close"
                  :disabled="isLoading"
                >Dismiss</v-btn>
                <v-btn 
                  flat 
                  color="green darken-1" 
                  @click="handleData"
                  :disabled="!valid || isLoading"
                >Login</v-btn>
                <v-progress-circular
                  v-show="isLoading"
                  indeterminate
                  color="grey darken-2"
                ></v-progress-circular>
              </v-card-actions>
            </v-card>
    </v-dialog>
</template>

<script>
    export default {
      data: () => {
          return {
            errors: [],
            isLoading: false,
            username: "",
            password: "",
            valid: true,
            dialog: false,
            passwordRules: [
              value => !!value || 'Required.',
              value => {
                if (value)
                  return value.length >= 8 || 'Min length is 8 symbols.'
                return true
              }
            ],
            usernameRules: [
              v => !!v || 'Required.'
            ]
        }
      },
      methods: {
        close() {
          this.$refs.form.resetValidation()
          this.dialog = false;
        },
        show() {
            this.dialog = !this.dialog;
        },
        handleData() {
          if (this.$refs.form.validate())
            this.isLoading = true;
        }
      }
    }
</script>
