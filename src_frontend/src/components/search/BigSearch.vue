<template>
    <v-form>
    <v-container >
        <v-layout justify-center row>
            <v-text-field
                class="search-field"
                v-model="message"
                append-outer-icon="send"
                
                clear-icon="clear"
                clearable
                label="What do you want to found?"
                type="text"
                @click:append-outer="sendMessage"
                @click:clear="clearMessage"
            ></v-text-field>
        </v-layout>
    </v-container>
    </v-form>
</template>

<script>
    export default {
        data: () => {
            return {
                show: false,
                message: '',
            }
        },

        computed: {
        },

        methods: {
            sendMessage: () => {
                this.clearMessage()
            },
            clearMessage: () => {
                this.message = ''
            },
        }
    }
</script>
