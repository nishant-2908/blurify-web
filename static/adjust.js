var options = document.getElementsByName("typeEdge");
var dynamic_container = document.getElementById("dynamic");
var preview = document.getElementById("previewButton");
var selectedValue = "";
options.forEach(function (option) {
    option.addEventListener("click", handleChange)
})

function handleChange() {
    for (var i = 0; i < options.length; i++) {
        if (options[i].checked) {
            selectedValue = options[i].value;
            preview.disabled = true;
            handleVisibility();
        }
    }
}

function handleVisibility() {
    if (selectedValue == "overall") {
        dynamic_container.innerHTML =
            `
        <div class="mb-3" id="all">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="overall-radius" class="col-form-label">Overall radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-overall" placeholder="Enter the overall radius" required>
                </div>
            </div>
        </div>
        `
        var inputs = dynamic_container.getElementsByTagName("input");
        Array.from(inputs).forEach(function (input) {
            input.addEventListener("input", function () {
                if (inputs[0].value > 0 || inputs[1].value > 0) {
                    preview.disabled = false;
                }
                else {
                    preview.disabled = true;
                }
            })
        })
    } else if (selectedValue == "vertical") {
        dynamic_container.innerHTML =
            `
        <div class="d-flex flex-row mb-3" id="vertical">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="top-radius" class="col-form-label">Top radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-top-v" placeholder="Enter the top radius"
                    required>
                </div>
            </div>
            <div class="row g-3 align-items-center ms-3">
                <div class="col-auto">
                    <label for="bottom-radius" class="col-form-label">Bottom radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-bottom-v" placeholder="Enter the bottom radius" required>
                </div>
            </div>
        </div>
        `
        var inputs = dynamic_container.getElementsByTagName("input");
        Array.from(inputs).forEach(function (input) {
            input.addEventListener("input", function () {
                if (inputs[0].value > 0 || inputs[1].value > 0) {
                    preview.disabled = false;
                }
                else {
                    preview.disabled = true;
                }
            })
        })
    } else if (selectedValue == "horizontal") {
        dynamic_container.innerHTML =
            `
        <div class="d-flex flex-row mb-3" id="horizontal">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="left-radius" class="col-form-label">Left radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-left-h" placeholder="Enter the left radius"
                    required>
                </div>
            </div>
            <div class="row g-3 align-items-center ms-3">
                <div class="col-auto">
                    <label for="right-radius" class="col-form-label">Right radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-right-h" placeholder="Enter the right radius"
                    required>
                </div>
            </div>
        </div>
        `
        var inputs = dynamic_container.getElementsByTagName("input");
        Array.from(inputs).forEach(function (input) {
            input.addEventListener("input", function () {
                if (inputs[0].value >= 0 && inputs[1].value >= 0) {
                    preview.disabled = false;
                } else if (inputs[0].value <= 0 && inputs[1].value <= 0) {
                    preview.disabled = true;
                }
                else {
                    preview.disabled = true;
                }
            })
        })
    } else if (selectedValue == "custom") {
        dynamic_container.innerHTML =
            `
        <div class="d-flex flex-row mb-3" id="custom">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="left-radius" class="col-form-label">Left radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-left" id="radius-left" placeholder="Enter the left radius" required>
                </div>
            </div>
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="bottom-radius" class="col-form-label">Bottom radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-bottom" id="radius-bottom" placeholder="Enter the bottom radius" required>
                </div>
            </div>
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="top-radius" class="col-form-label">Top radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-top" id="radius-top" placeholder="Enter the top radius" required>
                </div>
            </div>
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="right-radius" class="col-form-label">Right radius</label>
                </div>
                <div class="col-auto">
                    <input type="number" class="form-control" name="radius-right" id="radius-right" placeholder="Enter the right radius" required>
                </div>
            </div>
        </div>`
        var inputs = dynamic_container.getElementsByTagName("input");
        Array.from(inputs).forEach(function (input) {
            input.addEventListener("input", function () {
                if (inputs[0].value > 0 || inputs[1].value > 0 && inputs[2].value > 0 || inputs[3].value > 0) {
                    preview.disabled = false;
                }
                else {
                    preview.disabled = true;
                }
            })
        })
    }
}

handleChange();