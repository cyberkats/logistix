"use strict";

let map;

function initMap() {
  var melbourne = {lat: -37.813611, lng: 144.963056};
  map = new google.maps.Map(document.getElementById("map"), {
    center: melbourne,
    zoom: 8
  });
  var marker = new google.maps.Marker({
    position: {
      lat: -38.15,
      lng: 144.35
    }, map: map
  });
}
