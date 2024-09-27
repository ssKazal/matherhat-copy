$(document).ready(function () {

    var up_comming = ''

    for (let i = 0; i < 2; i++) {
        up_comming += `
        
        <div class="col-lg-6 col-12">
            <div class="up-comming-on-going-project-box">
                <div class="up-comming-on-going-project-img">
                    <img src="/static/design_related/assets/img/madrasa_img/gallery-2.jpg" alt="">

                    <div class="clip-box">
                        <i class="bi bi-paperclip"></i>
                    </div>
                </div>

                <div class="up-comming-on-going-project-padding">
                    <h1 class="up-comming-on-going-project-title">
                        It is a long established fact that a reader will be distracted by the readable content
                        of a
                        page when ...
                    </h1>

                    <div class="up-comming-on-going-project-progressing-box">
                        <div class="progress-percentage">
                            <span>80%</span>
                            <svg width="16" height="14" viewBox="0 0 16 14" fill="none">
                                <g filter="url(#filter0_d)">
                                    <path d="M3.63689 0.75L8 8.93689L12.3631 0.75H3.63689Z" stroke="#3CAC2A" />
                                </g>
                                <defs>
                                    <filter id="filter0_d" x="0.803955" y="0.25" width="14.3923" height="13.75"
                                        filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                                        <feFlood flood-opacity="0" result="BackgroundImageFix" />
                                        <feColorMatrix in="SourceAlpha" type="matrix"
                                            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" />
                                        <feOffset dy="2" />
                                        <feGaussianBlur stdDeviation="1" />
                                        <feColorMatrix type="matrix"
                                            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.27 0" />
                                        <feBlend mode="normal" in2="BackgroundImageFix"
                                            result="effect1_dropShadow" />
                                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow"
                                            result="shape" />
                                    </filter>
                                </defs>
                            </svg>

                        </div>
                        <div class="up-comming-on-going-project-progressing-bar">
                            <div style="width: 80%;" class="up-comming-on-going-project-progress"></div>
                        </div>
                    </div>

                    <div class="up-comming-on-going-project-info">
                        <p>
                            <b>Budget:</b>
                            <span>14,53,000 ৳</span>
                        </p>

                        <button class="green-btn" data-bs-toggle="modal" data-bs-target="#support-us-modal">
                            Support Us This Project
                        </button>

                        <p>
                            <b>Last Date:</b>
                            <span>23:06:2021</span>
                        </p>
                    </div>
                </div>

            </div>
        </div>
        `
    }

    $('#up-comming-project .row').append(up_comming)




})