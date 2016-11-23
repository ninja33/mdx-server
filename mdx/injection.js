//inhections.js

audio_type = {
    'mp3': 'audio/mpeg',
    'mp4': 'audio/mp4',
    'wav': 'audio/wav',
    'spx': 'audio/ogg',
    'ogg': 'audio/ogg'
}

function audio_content_type(ext){
    return audio_type[ext] || 'audio/mpeg'
    
}

$(document).ready(function(){
    $("body a").click(function(){
        var tag = $(this).attr("href");
        if (!tag) {
            return
        }
        if (tag.startsWith("sound://")) {
            $("#audiotag").attr("src", "/" + tag.substr("sound://".length));
            $("#audiotag").attr("type", audio_content_type(tag.slice(-3)));
            try {
                audioElement = document.getElementById("audiotag");
                audioElement.play()
            } catch (err) {
            }
            return
        }
    });
});
