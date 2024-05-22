file = document.getElementById("file")
directory = document.getElementById("directory")
button = document.getElementById("next-button")

directory.addEventListener("input", validateInputs);
file.addEventListener("input", validateInputs);

function validateInputs()
{
    if (file.value.trim() !== "" && directory.value.trim() !== "") 
    {
        var allowedExtensions = [".jpg", ".jpeg", ".png"];
    
        var fileName = file.value.trim().toLowerCase();
    
        var hasValidExtension = allowedExtensions.some(function(extension) {
          return fileName.endsWith(extension);
        });
    
        button.disabled = !hasValidExtension;
      } 
      else 
      {
        button.disabled = true;
      }
}