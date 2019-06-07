<template>
<div>
    <main-header/>
    <v-container  >
        <big-search v-on:startSearch="startSearch" />
        <div v-if="this.items.length != 0">
            <v-layout flex class="pt-0">
                <div class="headline pt-2">
                    Results:
                </div>
                <v-spacer />
                <div class="pt-2">
                    <v-btn icon class="ma-0">
                        <v-icon color="grey darken-1" medium>keyboard_arrow_left</v-icon>
                    </v-btn>
                    <v-btn icon class="ma-0">
                        <v-icon color="grey darken-1" medium>keyboard_arrow_right</v-icon>
                    </v-btn>
                </div>
            </v-layout>
            
            <v-divider color="grey" class="mb-2"/>

            <v-layout row wrap v-scroll="onScroll">
            <search-item v-for="item in this.items" :key="item.video_id"
                :item="item"/>
            <media-element ref="media"/>
            </v-layout>
            <v-btn
                v-show="displayReturnButton"
                fixed
                dark
                fab
                bottom
                right
                color="grey lighten-1"
                @click="returnToTop"
            >
                <v-icon color="black" large>keyboard_arrow_up</v-icon>
            </v-btn>
        </div>
    </v-container>
    <big-process ref="bigProcess" />
    <login-form ref="loginForm" />
    <register-form ref="registerForm" />
    <user-info ref="userInfo" />
    
  </div>  
</template>

<script>
    import BigSearch from '@/components/search/BigSearch';
    import SearchItem from '@/components/search/SearchItem';
    import MediaElement from '@/components/search/MediaElement';
    import Header from '@/components/main/Header';
    import LoginForm from "@/components/user/LoginForm";
    import RegisterForm from "@/components/user/RegisterForm";
    import UserInfo from "@/components/user/UserInfo";
    import BigProcess from "@/components/progress/BigProcess";

    export default {
        methods: {
            onScroll (e) {
                this.offsetTop = window.pageYOffset || document.documentElement.scrollTop
            },
            returnToTop() {
                this.$vuetify.goTo(0, {
                    duration: 200,
                    offset: 0,
                    easing: 'linear'
                });
            },
            setItems() {
                this.items = [
                    {
                        id: 1,
                        title: 'First',
                        description: 'first descr',
                        video_id: '_8aKKEjIO2g',
                        preview_url: 'https://i.ytimg.com/vi/_8aKKEjIO2g/hqdefault.jpg',
                        featured: false,
                    },
                    {
                        id: 2,
                        title: '"ぼく官3 成田WW StageS01 Good-bye and Hello!①"',
                        description: 'first descr',
                        video_id: 'RCNJP1juCbM',
                        preview_url: "https://i.ytimg.com/vi/RCNJP1juCbM/hqdefault.jpg",
                        featured: false,
                    },
                ]
                this.$refs.bigProcess.close();
            },

            startSearch(q) {
                this.isLoading = true;
                this.$refs.bigProcess.show();
                setTimeout(() => (this.setItems()), 2000);
            }
        },
        watch:{
            offsetTop (o, n) {
                if (n >= this.displayReturnButtonValue) {
                    this.displayReturnButton = true;
                } else {
                    this.displayReturnButton = false;
                }
            },
        },
        data: () => {
            return {
                displayReturnButtonValue: 200,
                displayReturnButton: false,
                offsetTop: 0,
                items: []
            }
        },
        computed: {
            isLoading() {
                return this.$store.state.isLoading;
            }
        },
        components: {
            'big-search':       BigSearch,
            'search-item':      SearchItem,
            'media-element':    MediaElement,
            'login-form':       LoginForm,
            'register-form':    RegisterForm,
            'user-info':        UserInfo,
            'main-header':      Header,
            'big-process':      BigProcess
        },
        beforeMount() {
            this.$store.dispatch('initial');
        }
    }
</script>
