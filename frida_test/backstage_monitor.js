
Java.perform(function() {
    var BroadcastReceiver = Java.use('com.bytedance.ug.share.utils.ShareSupportUtils$InstallOrUninstallReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.bytedance.ug.share.utils.ShareSupportUtils$InstallOrUninstallReceiver BroadcastReceiver" );
        }
        this.onReceive(context, intent);
    };
});


Java.perform(function() {
    var BroadcastReceiver = Java.use('com.ss.android.socialbase.appdownloader.DownloadReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.ss.android.socialbase.appdownloader.DownloadReceiver" );
        }
        this.onReceive(context, intent);
    };
});
Java.perform(function() {
    var BroadcastReceiver = Java.use('com.bytedance.news.ad.base.download.DownloadReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.bytedance.news.ad.base.download.DownloadReceiver" );
        }
        this.onReceive(context, intent);
    };
});
Java.perform(function() {
    var BroadcastReceiver = Java.use('com.ss.android.video.base.utils.InstallPackageUtils$InstallReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.ss.android.video.base.utils.InstallPackageUtils$InstallReceiver");
        }
        this.onReceive(context, intent);
    };
});
Java.perform(function() {
    var BroadcastReceiver = Java.use('com.ss.android.socialbase.appdownloader.DownloadReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.ss.android.socialbase.appdownloader.DownloadReceiver" );
        }
        this.onReceive(context, intent);
    };
});
Java.perform(function() {
    var BroadcastReceiver = Java.use('com.bytedance.usergrowth.data.deviceinfo.AppStatusBroadcastReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : com.bytedance.usergrowth.data.deviceinfo.AppStatusBroadcastReceiver BroadcastReceiver" );
        }
        this.onReceive(context, intent);
    };
});
Java.perform(function() {
    var BroadcastReceiver = Java.use('android.content.BroadcastReceiver');
    BroadcastReceiver.onReceive.implementation = function(context, intent) {
        var action = intent.getAction();
        if (action === 'android.intent.action.PACKAGE_ADDED' ||
            action === 'android.intent.action.PACKAGE_REMOVED') {
            showjavastack()
            console.log("original call : BroadcastReceiver" );
        }
        this.onReceive(context, intent);
    };
});
function showjavastack(){
    var javastack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
    console.log(javastack);
}