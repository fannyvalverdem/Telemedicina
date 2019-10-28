(function(){

	console.log('checkSystemRequirements');
	console.log(JSON.stringify(ZoomMtg.checkSystemRequirements()));

// it's option if you want to change the jssdk dependency link resources.
// ZoomMtg.setZoomJSLib('https://dmogdx0jrul3u.cloudfront.net/1.5.1/lib', '/av'); // CDN version default
// ZoomMtg.setZoomJSLib('https://source.zoom.us/1.5.1/lib', '/av'); // Global use source.zoom.us
// ZoomMtg.setZoomJSLib('https://jssdk.zoomus.cn/1.5.1/lib', '/av'); // China use jssdk.zoomus.cn   
// ZoomMtg.setZoomJSLib('http://localhost:9999/node_modules/zoomus-jssdk/dist/lib', '/av'); // Local version default

    ZoomMtg.preLoadWasm();

    ZoomMtg.prepareJssdk();
    
    var API_KEY = 'fRb1YgwnRT6ASYvVxSMwOg';

    /**
     * NEVER PUT YOUR ACTUAL API SECRET IN CLIENT SIDE CODE, THIS IS JUST FOR QUICK PROTOTYPING
     * The below generateSignature should be done server side as not to expose your api secret in public
     * You can find an eaxmple in here: https://marketplace.zoom.us/docs/sdk/native-sdks/Web-Client-SDK/tutorial/generate-signature
     */
    var API_SECRET = 't1CUHWdU2bzbVmL1aT9HFdfuke0SRP8Og6VZ';


        var meetConfig = {
            apiKey: API_KEY,
            apiSecret: API_SECRET,
            meetingNumber: 896339310,
            userName: "Paciente",
            passWord: "",
            leaveUrl: "http://www.google.com",
            role: 0
        };


        var signature = ZoomMtg.generateSignature({
            meetingNumber: meetConfig.meetingNumber,
            apiKey: meetConfig.apiKey,
            apiSecret: meetConfig.apiSecret,
            role: meetConfig.role,
            success: function(res){
                console.log(res.result);
            }
        });

        ZoomMtg.init({
            leaveUrl: 'http://www.google.com',
            isSupportAV: true,
            success: function () {
                ZoomMtg.join(
                    {
                        meetingNumber: meetConfig.meetingNumber,
                        userName: meetConfig.userName,
                        signature: signature,
                        apiKey: meetConfig.apiKey,
                        userEmail: 'email@gmail.com',
                        passWord: meetConfig.passWord,
                        success: function(res){
                            $('#nav-tool').hide();
                            console.log('join meeting success');
                        },
                        error: function(res) {
                            console.log(res);
                        }
                    }
                );
            },
            error: function(res) {
                console.log(res);
            }
        });

})();