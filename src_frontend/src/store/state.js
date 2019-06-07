const state = {
    isLoading:      false,
    user:           {
        token:          null,
        username:       '',
        email:          '',
        links:          []
    },
    requestData:    {
        data:           '',
        currPageToken:  null,
        nextPageToken:  null,
        prevPageToken:  null
    }
}

export default state;
