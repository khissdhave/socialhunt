document.querySelector('.more-icon').addEventListener('click', function() {
    document.querySelector('.popup').classList.toggle('show-popup');
});

// Close the popup when clicking outside the popup content
document.querySelector('.popup').addEventListener('click', function(event) {
    const popupContent = document.querySelector('.popup-content');
    if (!popupContent.contains(event.target)) {
        document.querySelector('.popup').classList.remove('show-popup');
    }
});
