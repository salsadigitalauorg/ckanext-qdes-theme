jQuery(document).ready(function () {
    jQuery(document).on('shown.bs.popover', '[data-target="popover"]', function () {
        jQuery(this).attr('data-popover-visible', '1');
    });
    jQuery(document).on('hidden.bs.popover', '[data-target="popover"]', function () {
        jQuery(this).attr('data-popover-visible', '0');
    });
    jQuery(document).on('click', function (e) {
        jQuery('[data-target="popover"],[data-original-title]').each(function () {
            if (!jQuery(this).is(e.target) && jQuery(this).has(e.target).length === 0 && jQuery('.popover').has(e.target).length === 0) {
                if (jQuery(this).attr('data-popover-visible') === '1') {
                    jQuery(this).click();
                }
            }
        });
    });
});
