$(document).ready(function () {
  var width = window.innerWidth || $(window).width();

  // slider
  $('.about-madrasha-slider').owlCarousel({
    nav: false,
    loop: true,
    autoplay: true,
    autoplayTimeout: 5000,
    autoplayHoverPause: true,
    items: 1,
  });

  $('.madrasha-gallery-box').click(function () {
    var gallery_img_src = $(this)
      .children('.madrasha-gallery-box-img')
      .children('img')
      .attr('src');
    var gallery_text = $(this).children('.madrasha-gallery-box-heading').text();

    $('.gallery-modal-open').fadeIn();
    $('body').css({
      overflow: 'hidden',
      'padding-right': width > 992 ? '17px' : 0,
    });

    $('.gallery-img img').attr('src', gallery_img_src);
    $('.gallery-modal-content p').text(gallery_text);
  });

  $('.gallery-close-icon').click(function () {
    var galley_modal = $(this).attr('modal-num');
    $('.gallery-modal-open').fadeOut();

    if (galley_modal == 'two') {
      $(this).removeAttr('modal-num');
    } else {
      $('body').css({
        'overflow-y': 'scroll',
        'padding-right': '0px',
      });
    }
  });

  $('[data-bs-target="#support-us-modal"]').click(function (e) {
    $('body').css({
      overflow: 'hidden',
      'padding-right': width > 992 ? '17px' : 0,
    });
  });

  $(document).mousedown(function (e) {
    var gallery_modal = $('.gallery-modal-content');
    var mobile_menu = $('.nav_bar ul');
    var top_var = $('.top-bar p');
    var support_us_modal_dialog = $('.support-us-modal-dialog .modal-content');
    var more_gallery_modal_content = $('.more-gallery-modal-content');

    if (
      !gallery_modal.is(e.target) &&
      !mobile_menu.is(e.target) &&
      !top_var.is(e.target) &&
      !support_us_modal_dialog.is(e.target) &&
      !more_gallery_modal_content.is(e.target) &&
      more_gallery_modal_content.has(e.target).length === 0 &&
      gallery_modal.has(e.target).length === 0 &&
      support_us_modal_dialog.has(e.target).length === 0
    ) {
      $('.gallery-modal-open').fadeOut();
      $('.more-gallery-modal').fadeOut();
      $('body').css({
        'overflow-y': 'scroll',
        'padding-right': '0px',
      });
    }
  });

  $('#modal_image_gellary').justifiedGallery({
    rowHeight: 200,
    lastRow: 'nojustify',
    margins: 15,
  });

  if (width < 992) {
    $('header').append(
      '<div class="menu-bi-list"> <i class="bi bi-list"></i> </div>'
    );
    $('.nav_bar ul').append(
      '<div class="menu-bi-x"> <i class="bi bi-x"></i> </div>'
    );
  }

  $(document).on('click', '.menu-bi-list', function () {
    $('.nav_bar ul').fadeIn();
    $('body').css({
      overflow: 'hidden',
    });
  });

  $(document).on('mousedown click', '.menu-bi-x', function () {
    mobile_menu_out();
  });

  if (width < 992) {
    $('.nav_bar ul li').click(function () {
      mobile_menu_out();
    });
  }

  function mobile_menu_out() {
    $('.nav_bar ul').fadeOut();
    $('body').css({
      'overflow-y': 'scroll',
    });
  }

  $('.gallery-see-more').click(function () {
    $('.more-gallery-modal').fadeIn();
    $('body').css({
      overflow: 'hidden',
      'padding-right': width > 992 ? '17px' : 0,
    });
  });

  $('.more-gallery-modal-close').click(function () {
    $('.more-gallery-modal').fadeOut();
    $('body').css({
      'overflow-y': 'scroll',
      'padding-right': '0px',
    });
  });

  $('.support-us-btn[data-bs-dismiss]').click(function () {
    $('body').css({
      'overflow-y': 'scroll',
    });

    $('.support-us-input-field input').val('');
    $('.support-us-textarea-field textarea').val('');
  });

  $('.modal-gallery_img_box').click(function () {
    var gallery_img_src = $(this).children('img').attr('src');
    var gallery_text = $(this).children('p').text();

    $('.gallery-close-icon').attr('modal-num', 'two');

    $('body').css({
      'overflow-y': 'scroll',
      'padding-right': '0px',
    });

    $('.gallery-modal-open').fadeIn();
    $('body').css({
      overflow: 'hidden',
      'padding-right': width > 992 ? '17px' : 0,
    });

    $('.gallery-img img').attr('src', gallery_img_src);
    $('.gallery-modal-content p').text(gallery_text);
  });

  $(document).scroll(function () {
    var height = $(window).scrollTop();

    if (height > 2000) {
      $('.go-top').fadeIn();
      $('.go-top').css({
        display: 'grid',
      });
    } else {
      $('.go-top').fadeOut();
    }
  });

  $(".go-top").click(function() {
    $("html, body").animate({ 
        scrollTop: 0 
    }, 10);
    return false;
  });

  // for csrf_token...
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');

  $(function () {
    $("form[name='contact-form']").validate({
      rules: {
        name: 'required',
        email: {
          required: function () {
            return !$('#phone').val();
          },
          email: true,
        },
        phone: {
          required: function () {
            return !$('#email').val();
          },
        },
        message: 'required',
        country: 'required',
        subject: 'required',
      },
      messages: {
        name: gettext('Please enter your name'),
        email: gettext('Please enter a valid email address'),
        phone: gettext('Please enter your phone'),
        message: gettext('Please leave your massage'),
        country: gettext('Please select your country'),
        subject: gettext('Please choose your subject'),
      },

      submitHandler: function (form) {
        var data = new FormData(form);
        $.ajax({
          method: 'POST',
          url: api_contactus_urls,
          dataType: 'json',
          headers: {
            'X-CSRFToken': csrftoken,
          },
          data : data,
          processData: false,
          contentType: false,
          beforeSend: function () {
            $('#spinner').removeClass('dissable');
          },
          complete: function () {
            $('#spinner').addClass('dissable');
          },
          success: add_success,
          error: add_error,
        });

        function add_success() {
          $('#contact-form').addClass('dissable');
          $('#success-message').removeClass('dissable');
          $('#go-back').removeClass('dissable');
          $('.back').click(function () {
            $('[data-bs-target="#support-us-modal"]').trigger('click');
            setTimeout(function () {
              $('.support-us-input-field input').val('');
              $('.support-us-textarea-field textarea').val('');
              $('#contact-form').removeClass('dissable');
              $('#success-message').addClass('dissable');
              $('#go-back').addClass('dissable');
            }, 1000);
          });
        }

        function add_error() {
          $('#contact-form').addClass('dissable');
          $('#error-message').removeClass('dissable');
          $('#try').removeClass('dissable');
          $('.now').click(function () {
            $('#contact-form').removeClass('dissable');
            $('#error-message').addClass('dissable');
            $('#try').addClass('dissable');
          });
          $('.later').click(function () {
            $('[data-bs-target="#support-us-modal"]').trigger('click');
            setTimeout(function () {
              $('#contact-form').removeClass('dissable');
              $('#error-message').addClass('dissable');
              $('#try').addClass('dissable');
            }, 1000);
          });
        }
      },
    });
  });
});
