<template>
    <v-layout justify-center>
        <v-flex xs12 lg6>
        <v-card>
            <v-flex d-flex>
                <v-flex xs4>
                    <v-img
                    :src="$props.preview_url"
                    max-height="200"

                    position="left"
                    aspect-ratio="1"
                    contain
                    >
                    <template v-slot:placeholder>
                        <v-layout
                        align-center
                        justify-center
                        ma-0
                        >
                        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                        </v-layout>
                    </template>
                    </v-img>
                </v-flex>
                <v-flex xs8>
                    <v-card-title >
                        <a @click.stop="showDialog($props.video_id)"> {{$props.title}} </a>
                    </v-card-title>

                    <v-card-text >
                    {{$props.description}}
                    </v-card-text>
                </v-flex>
            </v-flex>
        </v-card>
        </v-flex>
    </v-layout>
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
