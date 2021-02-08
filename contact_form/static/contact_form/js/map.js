function initMap() {
  const wilsons = { lat: 51.2381163, lng: 0.5613165 };

  const map = new google.maps.Map(document.getElementById("map"), {
    center: wilsons,
    zoom: 16,
  });

  const marker = new google.maps.Marker({
    position: wilsons,
    map: map,
  });


}