<template>
    <v-container fluid>
        <big-search />
        <search-item v-for="item in this.items" :key="item.video_id"
            :title="item.title" 
            :description="item.description" 
            :video_id="item.video_id"
            :preview_url='item.preview_url'/>
    </v-container>
</template>

<script>
    import BigSearch from '@/components/search/BigSearch';
    import SearchItem from '@/components/search/SearchItem';

    export default {
        data: () => {
            return {
                items: [
                    {
                        id: 1,
                        title: 'first',
                        description: 'first descr',
                        video_id: '_8aKKEjIO2g',
                        preview_url: 'https://i.ytimg.com/vi/_8aKKEjIO2g/hqdefault.jpg'
                    }
                ]
            }
        },
        components: {
            'big-search': BigSearch,
            'search-item': SearchItem,
        }
    }
</script>
