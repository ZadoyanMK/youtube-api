<template>
    
    <v-flex xs12 sm6 md4 lg3 class="pa-1">
        <v-hover>
        <v-card 
            slot-scope="{ hover }"
            :class="`elevation-${hover ? 12 : 2}`"
            class="search-card-item mx-auto"
        >
            <v-img
                class="white--text search-item-img"
                height="200px"
                :src="$props.item.preview_url"
                @click.stop="showDialog"
                >
                <v-container fluid pt-1 pr-1>
                    <v-layout justify-end row>
                        
                        <v-btn icon dark @click.stop="featured=!featured">
                            <v-icon :color="featured ? 'red' : 'white'" medium>favorite</v-icon>
                        </v-btn>
                    </v-layout>
                </v-container>
            </v-img>
            <v-card-title>
                <div>
                    <span class="font-weight-regular" :class="titleClass"> 
                        <a @click.stop="showDialog">{{$props.item.title}}</a>
                    </span>
                    <br>
                    <span class="grey--text">Number 10</span><br>
                </div>
            </v-card-title>
        </v-card>
        </v-hover>
    </v-flex>    
</template>

<script>
    export default {
        beforeMount(){
            this.featured = this.$props.item.featured;
        },

        props: ['item'],
        data: () => {
            return {
                dialog: false,
                featured: false,
            }
        },
        computed: {
            titleClass(){
                const titleLength = this.$props.item.title.length;

                if (titleLength > 30) {
                    return 'subheading';
                } else if (titleLength > 15) {
                    return 'title';
                }
                return 'headline';
            }
        },
        components: {
        },
        methods: {
            showDialog() {
                this.$parent.$refs.media.title=this.$props.item.title;
                this.$parent.$refs.media.show(this.$props.item.video_id);
            }
        }
    }
</script>
