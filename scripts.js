// Loading Screen
window.addEventListener('load', () => {
  setTimeout(() => {
      document.getElementById('loading').style.display = 'none';
      document.getElementById('content').style.display = 'block';
  }, 2000);
});

// Swiper Init
document.querySelectorAll('.swiper').forEach(swiperEl => {
  new Swiper(swiperEl, {
      loop: true,
      pagination: {
          el: swiperEl.querySelector('.swiper-pagination'),
          clickable: true,
      },
  });
});
