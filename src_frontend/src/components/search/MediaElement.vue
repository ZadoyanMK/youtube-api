<template>
    <v-dialog
        v-model="dialog"
        content-class="youtube-player"
    >
        <v-card>
            <v-card-title class="pb-2 pt-2 ml-3 mr-4">
                
                <div class="headline text-truncate">
                    {{title}}
                </div> 
                <!-- <v-layout row justify-end> -->
                    <!-- <v-spacer /> -->
                <v-btn icon @click="dialog = false" class="mr-0 media-close-btn">
                    <v-icon color="grey lighten-1" medium>clear</v-icon>
                </v-btn>
                <!-- </v-layout> -->
            </v-card-title>

        <youtube 
            :video-id="video_id" 
            @ready="ready" 
            @playing="playing" 
             />
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        data: () => {
            return {
                dialog: false,
                video_id: null,
                ready: true,
                playing: false,
                title: ''
            }
        },
        methods: {
            show: function(video_id) {
                this.dialog = !this.dialog;
                this.video_id = video_id;
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>