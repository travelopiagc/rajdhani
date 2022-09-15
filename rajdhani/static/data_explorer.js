const outputTable = new DataTable("#output-table", {
    columns: [], rows: []
})

const queryURL = "/db/exec"

function showError(err) {
    $("#errors").html(
        `<div class="alert alert-danger">
            ${err}
        </div>`
    )
}

function clearError() {
    $("#errors").html('')
}

async function execQuery(q) {
    const qs = getQuerystring({ q })
    const url = `${queryURL}?${qs}`

    const response = await fetch(url)
    return await response.json()
}

async function refreshOutput() {
    clearError()
    let q = $("#query").val()

    let response = undefined
    try {
        response = await execQuery(q)
    } catch (err) {
        showError(err)
        throw err
    }

    const { columns, rows } = response
    outputTable.refresh(rows, columns)
}

$(document).ready(function() {
    $("#btn-run").click(refreshOutput)
    $("#query").keydown(function(event) {
        if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
            refreshOutput()
        }
    })
})
