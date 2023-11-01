document.addEventListener('readystatechange', () => {
  if (document.readyState === 'complete') {
    document.querySelector('header').style.color = '#FF0000';
  }
});
