const mutations = {
    setLoadingStatus(state, p){
        state.isLoading = p;
    },
    setToken(state, payload){
        state.user.token = payload.token
    },
    setUser(state, payload) {
        state.user.email    = payload.user.email;
        state.user.username = payload.user.username;
        state.user.id       = payload.user.id;
        state.user.links    = payload.links;
    },
    setRequestData(state, payload) {
        state.setRequestData = {
            currPageToken:  payload.curr_page,
            nextPageToken:  payload.next_page,
            prevPageToken:  payload.prev_page,
            data:           payload.data
        }
    }
}

export default mutations;
