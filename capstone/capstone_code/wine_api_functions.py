function getUberAuthorization() {
return new Promise (function(resolve, reject) {
    var uberAuthorizationCode = $.ajax({
    type: 'GET',
    url: 'https://login.uber.com/oauth/v2/authorize',
    dataType: 'json',
    data: {
        response_type: 'code',
        client_id: uberClientId,
        client_secret: uberClientSercret

    },
    headers: {

    }
});
if (uberAuthorizationCode !== undefined) {
return resolve(uberAuthorizationCode);
} else {
reject(Error('Error - something is wrong!'));
}
});
};

function getUberToken(uberAuthorizationCode) {
return new Promise (function(resolve, reject) {
    var uberToken = $.ajax({
    type: 'POST',
    url: 'https://login.uber.com/oauth/v2/token',
    dataType: 'json',
    data: {
        client_secret: uberClientSercret,
        client_id: uberClientId,
        grant_type: 'authorization_code',
        code: uberAuthorizationCode.isString

    },
    headers: {

    }
});
if (uberToken !== undefined) {
return resolve(uberToken);
} else {
reject(Error('Error - something is wrong!'));
}
});
};
