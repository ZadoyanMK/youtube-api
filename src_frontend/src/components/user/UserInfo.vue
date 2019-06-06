<template>
    <v-dialog
        v-model="dialog"
        content-class="form-style"
        :persistent="isLoading"
        width="400"
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
                <v-card-text class="pb-0">
                    <blockquote class="blockquote pl-0 ">
                        <v-layout justify-center row>
                        <v-parallax
                            dark
                            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                            class="user-parallax-picture"
                        >
                            <v-layout
                            align-center
                            column
                            justify-center
                            >
                            <h1 class="display-2">{{username[0]}}</h1>
                            </v-layout>
                        </v-parallax>
                        </v-layout>
                    </blockquote>
                    <blockquote class="blockquote">
                        <b>Email:</b> {{email}}
                    </blockquote>
                    <blockquote class="blockquote">
                        <b>Username:</b> {{username}}
                    </blockquote>
                    <blockquote class="blockquote">
                        <a> Get featured list ({{featuredCount}}) </a>
                    </blockquote>
                    <!-- <blockquote class="blockquote"> -->
                        <ul>
                        <li class="red--text subheading" v-for="err in errors">
                            {{err}}
                        </li>
                        </ul>
                    <!-- </blockquote> -->
                
                </v-card-text>
                <v-card-actions class="pb-2">
                    <v-spacer />
                    <v-btn
                        flat 
                        color="primary" 
                        @click="logout"
                        :disabled="isLoading"
                    ><b>Log out</b></v-btn>
                    <v-progress-circular
                    v-show="isLoading"
                    indeterminate
                    color="grey darken-2"
                    ></v-progress-circular>
                    <v-spacer />
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
