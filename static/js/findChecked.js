
var checked_ids;

function findChecked() {
    let checkboxes = document.getElementsByTagName('input');
    let checked = Array();
    for (item of checkboxes) {
        if (item.checked) {
        checked.push(item.id);
        }
    }
    return checked;
};

function updateChecked() {
    let checked_ids = findChecked();
    $('#to_import').val(checked_ids);
};



