<template>
    <v-container fluid>
        <big-search />
        <v-layout row wrap>
        <search-item v-for="item in this.items" :key="item.video_id"
            :title="item.title" 
            :description="item.description" 
            :video_id="item.video_id"
            :preview_url='item.preview_url'/>
        <media-element ref="media"/>
        </v-layout>
    </v-container>
</template>

<script>
    import BigSearch from '@/components/search/BigSearch';
    import SearchItem from '@/components/search/SearchItem';
    import MediaElement from '@/components/search/MediaElement';

    export default {
        data: () => {
            return {
                items: [
                    {
                        id: 1,
                        title: 'First',
                        description: 'first descr',
                        video_id: '_8aKKEjIO2g',
                        preview_url: 'https://i.ytimg.com/vi/_8aKKEjIO2g/hqdefault.jpg'
                    },
                    {
                        id: 2,
                        title: '"ぼく官3 成田WW StageS01 Good-bye and Hello!①"',
                        description: 'first descr',
                        video_id: 'RCNJP1juCbM',
                        preview_url: "https://i.ytimg.com/vi/RCNJP1juCbM/hqdefault.jpg"
                    },
                    {
                        id: 3,
                        title: ' "Hello - หน้ากากเกอิชา | THE MASK SINGER หน้ากากนัก',
                        description: 'first descr',
                        video_id: 'bqEQTzNbL-I',
                        preview_url: "https://i.ytimg.com/vi/bqEQTzNbL-I/hqdefault.jpg"
                    }
                ]
            }
        },
        methods: {
        },
        components: {
            'big-search': BigSearch,
            'search-item': SearchItem,
            'media-element': MediaElement,
        }
    }
</script>
