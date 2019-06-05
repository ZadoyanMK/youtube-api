<template>
    <v-layout>
        <v-card>
            <v-card-title>
                {{$props.title}}
            </v-card-title>
        </v-card>
    </v-layout>
</template>

<script>
    export default {
        props: ['title', 'description', 'video_id', 'preview_url'],
        data: () => {
            return {

            }
        }

    }
</script>
