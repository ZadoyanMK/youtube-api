<template>
    <v-dialog
        v-model="dialog"
        content-class="form-style"
        :persistent="isLoading"
    >
        <v-card class="elevation-12">
              <v-toolbar color="grey lighten-2">
                <v-toolbar-title>User info</v-toolbar-title>
                <v-spacer />
                <v-btn 
                    icon 
                    @click="close" 
                    class="user-close-btn"
                    :disabled="isLoading">
                    <v-icon color="grey darken-1" medium>clear</v-icon>
                </v-btn>
              </v-toolbar>
              <v-card-text>
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
                    color="primary" 
                    @click="logout"
                    :disabled="isLoading"
                >Log out</v-btn>
                <v-progress-circular
                  v-show="isLoading"
                  indeterminate
                  color="grey darken-2"
                ></v-progress-circular>
              </v-card-actions>
            </v-card>
        <confirmation 
            v-on:confirm="confirmLogoutF"
            ref="confirmation"
        />
    </v-dialog>
</template>

<script>
    import LogoutConfirmation from '@/components/dialogs/LogoutConfirmation';
    export default {
        data: () => {
            return {
                errors: [],
                isLoading: false,
                username: "konzamir",
                dialog: false,
                email: "s@s.com",
                featuredCount: 29,
            }
        },
        watchers: {
            confirmLogout(o, n) {
                if (n) {
                    this.isLoading = true;
                }
            }
        },
        methods: {
            confirmLogoutF(confirmed){
                if (confirmed) {
                    this.isLoading = true;
                }
            },
          close() {
            this.dialog = false;
          },
          logout() {
              this.$refs.confirmation.show();
          },
          show() {
              this.dialog = !this.dialog;
          },
        },
        components: {
            'confirmation': LogoutConfirmation
        }
    }
</script>
