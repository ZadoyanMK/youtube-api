<template>
    
    <v-flex xs12 sm6 md4 lg3 class="pl-1 pb-2">
        <v-card>
            <v-img
                class="white--text"
                height="200px"
                :src="$props.preview_url"
                >
                <v-container fluid pt-1 pr-1>
                    <v-layout justify-end row>
                        <v-btn icon >
                            <v-icon color="white">favorite</v-icon>
                        </v-btn>
                    </v-layout>
                </v-container>
            </v-img>
            <v-card-title>
                <div>
                    <span class="headline"> <a @click.stop="showDialog($props.video_id)">{{$props.title}}</a></span><br>
                    <span class="grey--text">Number 10</span><br>
                </div>
            </v-card-title>
        </v-card>
    </v-flex>    
</template>

<script>
    export default {
        props: ['title', 'description', 'video_id', 'preview_url'],
        data: () => {
            return {
                dialog: false
            }
        },
        components: {
        },
        methods: {
            showDialog: function (video_id) {
                this.$parent.$refs.media.show(video_id);
            }
        }
    }
</script>
