"use strict";

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: -38.15,
      lng: 144.35
    },
    zoom: 8
  });
  var marker = new google.maps.Marker({
    position: {
      lat: -38.15,
      lng: 144.35
    }, map: map
  });
}
