
var images = imageContainer.getElementsByTagName("img");

function handleContainerClick(event) {
  var selectedValue = document.getElementById("terminals").value;

  var imageContainer = document.getElementById("imageContainer");

  // Check if an image with the same source already exists
  var existingImages = imageContainer.getElementsByTagName("img");
  for (var i = 0; i < existingImages.length; i++) {
    if (existingImages[i].getAttribute("data-source") === selectedValue) {
      // Image already exists, so prevent placing a duplicate
      var option = document.querySelector(
        'option[value="' + selectedValue + '"]'
      );
      option.disabled = true;
      return;
    }
  }

  var img = new Image();
  img.id = selectedValue;
  img.src = getImageSource(selectedValue);
  img.setAttribute("data-source", selectedValue);

  img.onload = function () {
    var containerRect = imageContainer.getBoundingClientRect();
    var offsetX = event.clientX - containerRect.left;
    var offsetY = event.clientY - containerRect.top;

    img.style.position = "absolute";
    img.style.left = offsetX - img.width / 2 + "px";
    img.style.top = offsetY - img.height / 2 + "px";

    imageContainer.appendChild(img);
  };
}

function getImageSource(selectedValue) {
  switch (selectedValue) {
    case "leftEye":
      return "images/lefteye.png";
    case "leftSocket":
      return "images/leftsocket.png";
    case "rightEye":
      return "images/righteye.png";
    case "rightSocket":
      return "images/rightsocket.png";
    case "mouse":
      return "images/mouse.png";
    default:
      return "";
  }
}


function clearImages() {
  var imageContainer = document.getElementById("imageContainer");
  imageContainer.innerHTML = "";
}


function checkTerminals() {
  var imageContainer = document.getElementById("imageContainer");
  var selectedValue = document.getElementById("terminals").value;
  
  // Получаем все изображения в контейнере
  var images = imageContainer.getElementsByTagName("img");
  
  var expectedElementCount = 5; // Ожидаемое количество элементов
  var placedElementCount = images.length; // Количество размещенных элементов
  
  // Проверяем, все ли элементы были размещены
  if (placedElementCount === expectedElementCount) {
    
  // Все элементы были размещены
  for (var i = 0; i < images.length; i++) {
  // Найдено изображение с выбранным значением, добавляем стиль границы
  images[i].style.border = "2px solid red";
  }
  lastResult = "Все элементы были размещены";
  } else {
  // Не все элементы были размещены
  lastResult = "Не все элементы были размещены";
  }

  try{
  var leftEye = document.getElementById("leftEye").getBoundingClientRect();
  var leftSocket = document.getElementById("leftSocket").getBoundingClientRect();
  var rightEye = document.getElementById("rightEye").getBoundingClientRect();
  var rightSocket = document.getElementById("rightSocket").getBoundingClientRect();
  var mouse = document.getElementById("mouse").getBoundingClientRect();

  var condition0 = leftSocket.top < mouse.top && leftSocket.bottom > leftEye.bottom && leftSocket.left < rightSocket.left;
  var condition2 = rightSocket.top < mouse.top && rightSocket.bottom > rightEye.bottom;
  if(condition0 && condition2) {lastResult+= "\nОбъект был распознан !"}
  else{lastResult+= "\nОбъект не распознан"};

  }
  catch(error){
  lastResult = "Не все элементы были размещены";
  }
  
  
  // Выводим результат проверки на странице
  var resultContainer = document.getElementById("resultContainer");
  resultContainer.innerHTML = lastResult;
  }

function searchImages() {
  var imageContainer = document.getElementById("imageContainer");
  var images = imageContainer.getElementsByTagName("img");

  // Выполнение действий с найденными изображениями
  for (var i = 0; i < images.length; i++) {
    var image = images[i];
    // Ваш код для обработки каждого изображения
  }
}