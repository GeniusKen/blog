window.onload = function () {
  toggleTop()
  backToTop()
  getMore()
}

function toggleTop () {
  $(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
      $('#blogTop').show()
    } else {
      $('#blogTop').hide()
    }
  })
}

function backToTop () {
  $('#blogTop').click(function () {
    window.scrollTo(0, 0)
  });
}

function getMore () {
  $('#blogMore').click(function () {
    var page = $(this).data('page')
    var size = $(this).data('size')
    var isAll = $(this).data('isAll')
    if (!isAll) {
      console.log(page, size)
      $.ajax({
        url: `/list`,
        type: 'post',
        data: { page: page, size: size },
        success: function (res) {
          console.log(res)
          if (res) {
            $('#blogMore').data('page', ++page)
            $('#blogContent').append(res)
          } else {
            $('#blogMore').html('没有更多文章了')
            $('#blogMore').data('isAll', true)
          }
        },
        error: function () {
          console.log('error')
        }
      })
    }
  })
}