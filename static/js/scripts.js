window.addEventListener('DOMContentLoaded', event => {

    const sidebarWrapper = document.getElementById('sidebar-wrapper');
    let scrollToTopVisible = false;
    // Closes the sidebar menu
    const menuToggle = document.body.querySelector('.menu-toggle');
    menuToggle.addEventListener('click', event => {
        event.preventDefault();
        sidebarWrapper.classList.toggle('active');
        _toggleMenuIcon();
        menuToggle.classList.toggle('active');
    })

    // Closes responsive menu when a scroll trigger link is clicked
    var scrollTriggerList = [].slice.call(document.querySelectorAll('#sidebar-wrapper .js-scroll-trigger'));
    scrollTriggerList.map(scrollTrigger => {
        scrollTrigger.addEventListener('click', () => {
            sidebarWrapper.classList.remove('active');
            menuToggle.classList.remove('active');
            _toggleMenuIcon();
        })
    });

    function _toggleMenuIcon() {
        // const menuToggleBars = document.body.querySelector('.menu-toggle > .fa-bars');
        // const menuToggleTimes = document.body.querySelector('.menu-toggle > .fa-list-ul');
        // if (menuToggleBars) {
        //     menuToggleBars.classList.remove('fa-bars');
        //     menuToggleBars.classList.add('fa-list-ul');
        // }
        // if (menuToggleTimes) {
        //     menuToggleTimes.classList.remove('fa-list-ul');
        //     menuToggleTimes.classList.add('fa-bars');
        // }
    }

    // Scroll to top button appear
    document.addEventListener('scroll', () => {
        const scrollToTop = document.body.querySelector('.scroll-to-top');
        if (document.documentElement.scrollTop > 100) {
            if (!scrollToTopVisible) {
                fadeIn(scrollToTop);
                scrollToTopVisible = true;
            }
        } else {
            if (scrollToTopVisible) {
                fadeOut(scrollToTop);
                scrollToTopVisible = false;
            }
        }
    })
})

function fadeOut(el) {
    el.style.opacity = 1;
    (function fade() {
        if ((el.style.opacity -= .1) < 0) {
            el.style.display = "none";
        } else {
            requestAnimationFrame(fade);
        }
    })();
};

function submitNewsletter() {
    var val = document.getElementById('newsletter').value;
    var invalidEmail = document.querySelector(".invalidEmail");
    var exist = document.querySelector(".exist");
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // // Get the <span> element that closes the modal
    // var span = document.getElementsByClassName("close")[0];
    // console.log(val)
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (val !== '' && val.match(mailformat)) {
        invalidEmail.style.display = "none";
        exist.style.display = "none";
        modal.style.display = "none";
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function() {
            console.log(JSON.parse(this.responseText)['data']);
            if (JSON.parse(this.responseText)['data'] !== 'OK') {
                exist.style.display = "block";
                // swal("Thanks You For Joining!", "", "success")
            } else {
                // btn.onclick = function() {
                modal.style.display = "block";
                // }
                // swal("THANK YOU FOR JOINING!", "", "success")
                document.getElementById("newsletter").innerHTML = this.responseText;
            }

        }
        xhttp.open("GET", "newletter?email_id=" + val);
        xhttp.send();
    } else {
        exist.style.display = "none";
        invalidEmail.style.display = "block"
        modal.style.display = "none";
    }
}

function fadeIn(el, display) {
    el.style.opacity = 0;
    el.style.display = display || "block";
    (function fade() {
        var val = parseFloat(el.style.opacity);
        if (!((val += .1) > 1)) {
            el.style.opacity = val;
            requestAnimationFrame(fade);
        }
    })();
};