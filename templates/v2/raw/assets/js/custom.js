var psy = document.getElementById('psychoid');

var psydata = document.getElementById('modalpsyid');

var psyclose = document.getElementById('psyclose');

psy.onclick = function(){
    psydata.style.display = "block";
}

psyclose.onclick = function(){
    psydata.style.display = 'none';
}