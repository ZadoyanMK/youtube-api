<template>
    <v-dialog
        v-model="dialog"
        width="600"
        height="300"
        dark
    >
        <v-card>
            <youtube 
                :video-id="video_id" 
                :player-width="'600'" 
                :player_height="'330'" 
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