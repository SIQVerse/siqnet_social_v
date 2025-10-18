const ctx = document.getElementById('chart').getContext('2d');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Views', 'Likes', 'Shares'],
    datasets: [{
      label: 'Engagement',
      data: [120, 45, 30],
      backgroundColor: ['blue', 'green', 'orange']
    }]
  }
});
